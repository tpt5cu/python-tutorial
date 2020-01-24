def unresolved_import():
    import module_.import_.import_processing.resolved_import.imported_state.target as target
    print('Unresolved observer import sees: {}'.format(target.target_list))
    print('Unresolved observer import sees: {}'.format(target.target_var))


def resolved_import():
    from module_.import_.import_processing.resolved_import.imported_state.target import target_list
    from module_.import_.import_processing.resolved_import.imported_state.target import target_var
    print('Resolved observer import sees: {}'.format(target_list))
    print('Resolved observer import sees: {}'.format(target_var))