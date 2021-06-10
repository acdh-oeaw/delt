# create_fixtures.sh

# make sure you ran `pip install django-fixture-magic` and added `'fixture_magic'` to INSTALLED_APPS
#source bin/activate

echo "create fixtures for text"
python manage.py dump_object assignments.text 1758 1757 --settings=delt.settings.local > fixture_text.json

echo "create fixtures for learnerprofile"
python manage.py dump_object assignments.learnerprofile 616 615 --settings=delt.settings.local > fixture_learnerprofile.json

echo "create fixtures for coursegroup"
python manage.py dump_object assignments.coursegroup '*' --settings=delt.settings.local > fixture_coursegroup.json

echo "create fixtures for learner"
python manage.py dump_object assignments.learner 126 124 --settings=delt.settings.local > fixture_learner.json

echo "create fixtures for assignment"
python manage.py dump_object assignments.assignment 5 3 --settings=delt.settings.local > fixture_assignment.json

echo "create fixtures for assignmentbaseclass"
python manage.py dump_object assignments.assignmentbaseclass 124 5 --settings=delt.settings.local > fixture_assignment_base_class.json

echo "create fixtures for place"
python manage.py dump_object assignments.place 127 125 --settings=delt.settings.local > fixture_place.json

echo "create fixtures for institution"
python manage.py dump_object assignments.institution 1128 1119 --settings=delt.settings.local > fixture_institution.json

echo "create fixtures for person"
python manage.py dump_object assignments.person 44 4 --settings=delt.settings.local > fixture_person.json

echo "create fixtures for participant"
python manage.py dump_object assignments.participant 1754 1755 --settings=delt.settings.local > fixture_participant.json

echo "create fixtures for textversion"
python manage.py dump_object assignments.textversion 3435 3436 --settings=delt.settings.local > fixture_textversion.json

echo "merge fixtures"
python manage.py merge_fixtures fixture_assignment_base_class.json fixture_assignment.json fixture_coursegroup.json fixture_institution.json fixture_learner.json fixture_learnerprofile.json fixture_participant.json fixture_person.json fixture_place.json fixture_text.json fixture_textversion.json --settings=delt.settings.local > assignments/fixtures/dump.json

echo "delete fixtures"
rm fixture_person.json
rm fixture_participant.json
rm fixture_textversion.json
rm fixture_institution.json
rm fixture_place.json
rm fixture_assignment_base_class.json
rm fixture_assignment.json
rm fixture_learner.json
rm fixture_coursegroup.json
rm fixture_learnerprofile.json
rm fixture_text.json

echo "done"
