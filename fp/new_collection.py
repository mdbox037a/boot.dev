def new_collection(initial_docs):
    copy_docs = initial_docs.copy()
    def add_to_collection(doc):
        copy_docs.append(doc)
        return copy_docs
    return add_to_collection