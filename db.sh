#!/bin/bash

pg_restore -c --host='db.gzdbtsojbmerkmkjkamj.supabase.co' --port=6543 --username="postgres" --dbname="postgres" --role="postgres" --password --verbose "/workspaces/Primary/university.tar"
pg_restore -c --host='localhost' --port=5432 --username="postgres" --dbname="flis" --role="root" --password --verbose "flisdb.tar"