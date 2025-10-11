def count_nested_levels(nested_documents, target_document_id, level=1):
    local_level = level
    for document_id in nested_documents:
        if document_id == target_document_id:
            return local_level
        else:
            r_level = count_nested_levels(
                nested_documents[document_id], target_document_id, (local_level + 1)
            )
            if r_level != -1:
                return r_level

    return -1
