#!/bin/bash

echo "Running inside /app/prestart.sh:"

echo "
#!/bin/bash
# Let the DB start
#sleep 10;
# Run migrations
$(alembic -c /app/src/alembic.ini upgrade head)
"