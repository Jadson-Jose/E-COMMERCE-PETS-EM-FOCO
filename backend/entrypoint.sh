echo "Aguardando PostgreSQL ficar disponível..."
while ! nc -z db 5432; do
    sleep 0.1
done
echo "PostgreSQL disponível"

python manage.py migrate
python manage.py collectstatic --noinput

exec "$@"