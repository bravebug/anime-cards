from sqlalchemy.exc import IntegrityError

from app.db import engine, session_factory
from app.models.characters import Characters, Base
import requests

def load_characters(anime_name: str):
    url = 'https://shikimori.one/api/graphql'
    data = """
    {
  # look for more query params in the documentation
  animes(search: "naruto", limit: 1, kind: "!special") {

    characterRoles {
      id
      rolesRu
      rolesEn
      character { id name poster { mainUrl } description }
    }

  }
}"""
    response = requests.post(
        url,
        json={"query": data},
        headers={'User-Agent': 'Python'})
    anime_chars = response.json()['data']['animes'][0]['characterRoles']
    create_db(anime_chars)


def create_db(data):
    Base.metadata.create_all(engine)
    with session_factory() as session:
        for item in data:
            try:
                character = Characters(
                    id=item.get('id'),
                    name=item.get('character', {}).get('name'),
                    description=item.get('character', {}).get('description', ' '),
                    image=item.get('character', {}).get('poster', {}).get('mainUrl'),
                    role=next(iter(item.get('rolesEn', [])))
                )
                session.add(character)
                session.commit()
            except AttributeError:
                pass
            except IntegrityError:
                session.rollback()


if __name__=='__main__':
    chars = load_characters('naruto')