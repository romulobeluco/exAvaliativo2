from neo4j import GraphDatabase

class Database:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def query(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return [record for record in result]

db = Database("bolt://localhost:7606", "neo4j", "senha")


def get_teacher_renzo():
    query = """
    MATCH (t:Teacher {name: 'Renzo'})
    RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf
    """
    return db.query(query)


def get_teachers_starting_with_m():
    query = """
    MATCH (t:Teacher)
    WHERE t.name STARTS WITH 'M'
    RETURN t.name AS name, t.cpf AS cpf
    """
    return db.query(query)


def get_all_cities():
    query = """
    MATCH (c:City)
    RETURN c.name AS name
    """
    return db.query(query)


def get_schools_in_range():
    query = """
    MATCH (s:School)
    WHERE s.number >= 150 AND s.number <= 550
    RETURN s.name AS name, s.address AS address, s.number AS number
    """
    return db.query(query)


def get_youngest_and_oldest_teacher():
    query = """
    MATCH (t:Teacher)
    RETURN MIN(t.ano_nasc) AS oldest, MAX(t.ano_nasc) AS youngest
    """
    return db.query(query)


def get_average_population():
    query = """
    MATCH (c:City)
    RETURN AVG(c.population) AS average_population
    """
    return db.query(query)


def get_city_by_cep():
    query = """
    MATCH (c:City {cep: '37540-000'})
    RETURN REPLACE(c.name, 'a', 'A') AS name
    """
    return db.query(query)


def get_teachers_third_letter():
    query = """
    MATCH (t:Teacher)
    RETURN SUBSTRING(t.name, 2, 1) AS third_letter
    """
    return db.query(query)
