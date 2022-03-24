// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "./SimpleStorage.sol";

contract StorageFactory{
    SimpleStorage[] public StorageArray;
    function createContract() public {
        SimpleStorage myStorage = new SimpleStorage();
        StorageArray.push(myStorage);
    }
    function call_update(uint _index, uint _data) public {
        SimpleStorage(address(StorageArray[_index])).updateStorage(_data);
    }
    function call_retrieve(uint _index) public view returns(uint){
        return SimpleStorage(address(StorageArray[_index])).retrieveStorage();
    }
}