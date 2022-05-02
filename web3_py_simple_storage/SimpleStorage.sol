// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

contract SimpleStorage{

    // This'll get initialized to 0!
    uint256 favoriteNumber;

    struct People{
        uint256 favoriteNumber;
        string name;
    }

    People[] public people;
    mapping(string => uint256) public nameToFavoriteNumber;

    function store(uint256 _favoriteNumber) public returns (uint256){
        favoriteNumber = _favoriteNumber;
        return _favoriteNumber;
    }

    // view, pure
    function retrieve() public view returns(uint256){
        return favoriteNumber;
    }

    // memory stores only during runtime, storage stores even after function execution 
    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People(_favoriteNumber, _name));
        nameToFavoriteNumber[_name]= _favoriteNumber;
    }
}