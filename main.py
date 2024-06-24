import click
from query import Database
from teacher_crud import TeacherCRUD

db = Database("bolt://localhost:7606", "neo4j", "senha")
teacher_crud = TeacherCRUD(db)

@click.group()
def cli():
    pass

@click.command()
def create_teacher():
    name = 'Chris Lima'
    ano_nasc = 1956
    cpf = '189.052.396-66'
    teacher_crud.create(name, ano_nasc, cpf)
    click.echo(f'Teacher {name} created.')

@click.command()
def read_teacher():
    name = 'Chris Lima'
    teacher = teacher_crud.read(name)
    click.echo(f'Teacher details: {teacher}')

@click.command()
def update_teacher():
    name = 'Chris Lima'
    newCpf = '162.052.777-77'
    teacher_crud.update(name, newCpf)
    click.echo(f'Teacher {name} updated.')

@click.command()
def delete_teacher():
    name = 'Chris Lima'
    teacher_crud.delete(name)
    click.echo(f'Teacher {name} deleted.')

cli.add_command(create_teacher)
cli.add_command(read_teacher)
cli.add_command(update_teacher)
cli.add_command(delete_teacher)

if __name__ == '__main__':
    cli()
