def json_extract(obj, key):
    """Recursively fetches values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively searches for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key and len(v.split()) != 1:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values
    