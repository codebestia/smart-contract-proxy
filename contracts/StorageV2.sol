// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StorageV2 {
    uint256 number;
    function setNumber(uint256 _number) public{
        number = _number;
    }
    function getNumber() public view returns(uint256){
        return number;
    }
    function increment() public {
        number = number + 1;
    }
    function decrement() public {
        if( number > 0){
            number = number - 1;
        }
    }
}
