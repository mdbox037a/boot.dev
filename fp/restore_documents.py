def restore_documents(originals, backups):
    # attempt to complete in one line
    return set(
        list(
            filter(lambda y: not y.isdigit(), list(map(lambda x: x.upper(), originals)))
        )
        + list(
            filter(lambda z: not z.isdigit(), list(map(lambda w: w.upper(), backups)))
        )
    )
