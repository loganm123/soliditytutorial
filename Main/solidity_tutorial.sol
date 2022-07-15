pragma solidity >= 0.6.0 < 0.9.0;

contract SimpleStorage {
    //this will get initiatialized to 0!
    //this is a comment
    //public keyword defines visibility
    //public functions can be called by anyone
    //variables are a function call
    //external function can only be called by someone external to a contract
    //private is they are only visible for the contract they are defined in
    //1:45:11
    uint256 public favoriteNumber;

    //this is a function
    function store(uint256 _favoriteNumber) public {
        //sets whatever the favorite number is for the favorite number
        favoriteNumber = _favoriteNumber;
    }

}