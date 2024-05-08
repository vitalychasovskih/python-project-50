from gendiff.commands.gendiff import generate_diff


def test_generate_diff():
    with open('tests/fixtures/expected1.txt', 'r') as e1:
        str = e1.read()
        assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures'
                                                          '/file2.json') == str
        assert generate_diff('tests/fixtures/file2.json', 'tests/fixtures'
                                                          '/file1.json') != str
        assert generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures'
                                                          '/file2.yml') == str
