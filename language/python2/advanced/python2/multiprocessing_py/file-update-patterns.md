- https://blog.gocept.com/2013/07/15/reliable-file-updates-with-python/

# ACID
- The goal of any file update operation it to follow the ACID properties:
    - Atomic: the update succeeds or fails entirely
    - Consistent: the file goes from one valid state to another
        - Internal consistency: the data structures of the file are consistent
        - External consistency: the file's contents are aligned with other data that relates to it
            - A common need is to update several different files in sync with each other
                - This can be done by designating a single file to lock an entire directory
                    - The scalability of this approach is limited b/c we have to have control over all readers (remember that locks are only advisory)
                      and only a single writer can operate on the entire directory at a time
                - Alternatively, use the write-replace pattern for entire directories. A directory exists for each update to a SET of files. The
                  latest consistent versions of the files are accessed through a symlink that is changed to the latest directory as soon as it has
                  been updated.
                    - It is important that the symlink is only changed once ALL the files in a directory have finished updating, and that the files
                      are accessed by cd-ing into that directory instead of accessing the files by their full path names. If the files are accessed
                      through their full path names, then the symlink could switch between one of those path traverals and I'd be accessing the old
                      version of file1 but the new version of file2 (see source example)
    - Isolated: running a set of transactions concurrently or in sequence will always give the same result
        - File locks are used to serialize file updates
    - Durability: data must be written to non-volatile storage before the user is informed of success
        - See the end of the source for notes on durability

# Truncate-write
- This file update pattern opens a file in "r+" mode, reads the file, does something with the data, seeks back to byte 0, truncates the file, and then
  writes the output
- Advantages
    - Simplifies locking becuase we only open the file one time
- Atomicity
    - This operation is not atomic. Right after the truncate operation, the file is empty and has no content at all.
        - If a concurrent process reads the file, it won't see the old or new version of the file
        - If an exception occurs after the truncate operation, the file will be left in an itermitant state
- Consistency
    - Atomicity is a prerequisite for consistency, so this operation is not consistent either
- Isolation
    - This pattern makes it easy to enforce isolation because we can use read and write locks on file. Just acquire the proper lock type on the file
      after opening it in "r+" mode and before truncating it
        - Unfortunately, I know that file corruption still occurs with this approach!

# Write-replace
- This pattern writes the data to an entirely new temporary file, then replaces the original file with the temporary file
- Advantages
    - More robust against errors than the truncate-write pattern
- Atomicity
    - The os.rename() function is atomic. Therefore, this file update pattern is also atomic
        - If an exception occurs while writing the temporary file, the rename operation will never occur. Thus, it's impossible to overwrite a
            old, valid file with a new, invalid one
        - Any process will see either the old file or the new file, but never some itermitant state
- Consistency
    - See ACID section. Additionally, the atomic nature of this pattern should provide single-file consistency
- Isolation
    - File locking can be used in this pattern too. However, it's a bit more complicated. See the source.

# Append
- Only open a file in order to append data to it
- Advantages
    - Simple to implement
- Atomicity
    - Not atomic because we could append incomplete records
        - We can counteract this by adding a checksum to each written record. When reading the records later on, discard those that lack a valid
          checksum
            - The original checksum would have been calculated by applying a cryptographic hash to the entire data record. When we READ the record
              again later on, we use the same cryptographic hash on the record. If the new hash doesn't match the old hash, discard the record.
- Consistency
    - ?
- Isolation
    - File locking is done the same as it is in the truncate-write pattern

# Spooldir
- Use a directory to store stuff. It's similar to the append strategy. Each update to a file is actually written to a new file inside the same
  directory
- Atomicity:
    - Similar to append, individual files in the spooldir approach can have a checksum
        - Alternatively, write each file in its entirety before moving it to its final location in a directory. This is borrowing from the
          write-replace pattern. This approach might be easier than using a checksum
- Consistency
    - ?
- Isolation
    - This pattern does not require file locking. However, a successful implementation depends on the underlying properties of 1) unique filename
      generation and 2) a naming scheme that communicates all necessary metadata about a file version