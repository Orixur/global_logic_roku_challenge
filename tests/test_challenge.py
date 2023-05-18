import pytest

import challenge


class TestC1:
    def test_correct_input(self):
        input = [1,2,3]
        
        res = challenge.problem_1(input)

    def test_incorrect_input(self):
        input = ['other', 'list', 'values', 'but', 'integers']

        with pytest.raises(ValueError):
            res = challenge.problem_1(input)

    def test_e1(self):
        input = [9]

        res = challenge.problem_1(input)

        assert res == [1,0]

    def test_e2(self):
        input = [19]

        res = challenge.problem_1(input)

        assert res == [2,0]

    def test_e3(self):
        input = [1,2,3]

        res = challenge.problem_1(input)

        assert res == [1,2,4]


class TestC2:
    def test_correct_input(self):
        input = '()[]{}'
        
        res = challenge.problem_2(input)

    def test_incorrect_input(self):
        input = 'other thing than allowed characters'

        with pytest.raises(ValueError):
            res = challenge.problem_2(input)

    def test_e1(self):
        input = '()'

        res = challenge.problem_2(input)

        assert res == True

    def test_e2(self):
        input = "()[]{}"

        res = challenge.problem_2(input)

        assert res == True

    def test_e3(self):
        input = '(]'

        res = challenge.problem_2(input)

        assert res == False

    def test_e4(self):
        input = '()(]()'

        res = challenge.problem_2(input)

        assert res == False

    def test_e5(self):
        input = '()()(]'

        res = challenge.problem_2(input)

        assert res == False

    def test_e6(self):
        input = '()()()'

        res = challenge.problem_2(input)

        assert res == True

    def test_e7(self):
        # Used as regression for Rule 2 of the problem
            # The first implementation checked the first item to be: "n==0 or c in openers"
        input = '([]{})'

        res = challenge.problem_2(input)

        assert res == False
