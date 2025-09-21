def generate_unique_id(existing_ids):
    """
    Generate a unique ID that doesn't exist in the provided list of IDs.
    
    :param existing_ids: List of existing IDs (integers).
    :return: A unique integer ID.
    """
    if not existing_ids:
        return 100
    return max(existing_ids) + 100