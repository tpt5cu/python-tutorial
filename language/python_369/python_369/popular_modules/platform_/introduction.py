# https://docs.python.org/3.6/library/platform.html 


import platform


def get_operating_system_information():
    print(platform.system()) # Darwin
    print(platform.version()) # Darwin Kernel Version 17.7.0: Thu Jan 23 07:05:23 PST 2020; root:xnu-4570.71.69~1/RELEASE_X86_64
    print(platform.platform()) # Darwin-17.7.0-x86_64-i386-64bit
    # mac_ver() returns (<release>, <versioninfo>, <machine>)
    # - <versioninfo> ::= (<version>, <dev_stage>, <non_release_version>)
    print(platform.mac_ver()) # ('10.13.6', ('', '', ''), 'x86_64')


if __name__ == '__main__':
    get_operating_system_information()
