import pytest
from pets import *


class TestDog:

    def test_dog_created_correctly(self):
        ## Set up the test
        color = 'Golden'
        my_dog = Dog(color)

        ## Check that everything was initialized properly
        assert my_dog.color == color
        assert my_dog.jump_count == 0

    def test_dohappy_pathg_(self):
        ## Set up the test
        my_dog = Dog("blue")

        ## Do the thing to test
        actual_color = my_dog.color

        ## Check that actual equals expected
        assert actual_color == "blue"

    def test_dog_jump(self):
        ## Setup
        my_dog = Dog("gray")

        ## Do the thing to test
        my_dog.jump()

        ## Assert/check that the actual equals expected
        assert my_dog.jump_count == 1


class TestHusky:

    def test_husky_created_correctly(self):
        ## Setup
        dubs = Husky()

        ## Check Assertions
        assert dubs.color == 'Gray'
        assert dubs.jump_count == 0

    def test_does_my_husky_jump(self):
        ## Setup
        my_dog = Husky()

        ## Run the thing we're testing
        my_dog.jump()

        ## Check our assertions
        assert my_dog.jump_count == 10

