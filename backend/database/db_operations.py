from database.models import Subject, Topic, Source


def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance


def get_or_create_subject(session, name):
    return get_or_create(session, Subject, name=name)


def get_or_create_topic(session, name, subject_str=None):
    instance = session.query(Topic).filter_by(name=name).first()
    if instance:
        return instance
    else:
        subject = get_or_create_subject(session, subject_str)
        instance = Topic(name=name, subject=subject)
        session.add(instance)
        session.commit()

        return instance


def get_or_create_source(session, name):
    return get_or_create(session, Source, name=name)

