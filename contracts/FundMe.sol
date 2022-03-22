// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FundMe {
    mapping (address => uint) address2amount;
    function recvFund() public payable {
        address2amount[msg.sender] += msg.value;
    }
}