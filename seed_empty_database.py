from data_access import create_database_if_it_doesnt_exist
from data_access.models import (
    OAuthTokenType as OATT_da,
    MicrosoftScopeUri as MSURI_da,
    MicrosoftScope as MS_da,
    GoogleScopeUri as GSURI_da,
    GoogleScope as GS_da,
    SessionFactory as Session,
)
from glue import (
    TokenType as OATT_glue,
    MicrosoftScopeURI as MSURI_glue,
    MicrosoftScope as MS_glue,
    GoogleScopeURI as GSURI_glue,
    GoogleScope as GS_glue,
)


def seed_empty_database():
    create_database_if_it_doesnt_exist()

    with Session() as session:
        for token_type in OATT_glue:
            model = OATT_da(name=token_type.value)
            session.add(model)
            session.commit()

        microsoft_uris = dict()
        for uri in MSURI_glue:
            model = MSURI_da(uri=uri.value)
            microsoft_uris[uri.value] = model

            session.add(model)
            session.commit()

        microsoft_scopes = dict()
        for scope in MS_glue:
            model = MS_da(name=scope.value)
            microsoft_scopes[scope.value] = model
            for uri in scope.uris:
                model.uris.append(microsoft_uris[uri.value])

            session.add(model)
            session.commit()

        google_uris = dict()
        for uri in GSURI_glue:
            model = GSURI_da(uri=uri.value)
            google_uris[uri.value] = model

            session.add(model)
            session.commit()

        google_scopes = dict()
        for scope in GS_glue:
            model = GS_da(name=scope.value)
            google_scopes[scope.value] = model
            for uri in scope.uris:
                model.uris.append(google_uris[uri.value])

            session.add(model)
            session.commit()


if __name__ == "__main__":
    # seed_empty_database()
    pass
