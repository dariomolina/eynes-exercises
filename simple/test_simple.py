from simple import simple_list, sort_list

def test_simple_list_len():
    persons = simple_list()
    assert len(persons) == 10, f"Expected 10 persons but got {len(persons)}"

def test_simple_list_keys():
    persons = simple_list()
    for person in persons:
        keys = ['id','age']
        keys_missing = []
        for key in keys:
            if key not in person.keys():
                keys_missing.append(key)
        assert len(keys_missing) == 0, f"Missing keys {keys_missing} in person: {person}"

def test_simple_list_age():
    persons = simple_list()
    for person in persons:
        assert isinstance(person["age"],int), f"Expected 'age' to be int but got {type(person['age'])}"
        assert 1 <= person["age"] <= 100, f"Expected 'age' to be 1-100 but got {person['age']}"

def test_sort_list():
    persons = sort_list(simple_list())
    for x in range(len(persons)-1):
        person1 = persons[x]
        person2 = persons[x+1]
        assert person1["age"] <= person2["age"], f"List is not properly sorted at index {x}"