from get import get_ as get

def get_test_succeed():
    assert get({'a': 1}, 'a', 0) == 1

def get_test_fail():    
    assert get({'a': 1}, 'a', 0) == 0
    
def get_test_fail_string():
    assert get({'a': 1}, 'a', 'hi') == 'hi'

if __name__ == "__main__":
    get_test_succeed()
    get_test_fail()
    get_test_fail_string()
