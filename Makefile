install: 
	poetry install
make build: 
	poetry build
publish: 
	poetry publish --dry-run
package-install: 
	python3 -m pip install --ignore-installed --user dist/*whl
gendiff: 
	poetry run gendiff