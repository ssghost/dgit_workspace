// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 myNumber = 1024;
    int256 myNegNumber = -1024;
    bool myBool = true;
    string myString = "Hello, world.";
    address myAddress = 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4;
    bytes32 myBytes = "eth";

    uint public storedData;
    function updateStorage(uint _storedData) public {
        storedData = _storedData;
    }
    function updateStorage_pri() private pure {
        uint storedData_pri = 1024;
    }
    function retrieveStorage() public view returns(uint){
        return storedData;
    }
    
    struct Account {
        string name;
        uint amount;
        address wallet;
    }
    Account public myaccount = Account({
        name: "vitalik",
        amount: 100,
        wallet: 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4
    });

    Account[] public asset;
    mapping(string => uint) public name2amount;
    function addAccount(string memory _name, uint _amount, address _wallet) public {
        asset.push(Account(_name, _amount, _wallet));
        name2amount[_name] = _amount;
    }

}
