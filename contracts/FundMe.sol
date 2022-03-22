// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract FundMe {
    mapping (address => uint) address2amount;
    function recvFund() public payable {
        uint minUSD = 5*10**8;
        require(getUSDRate(msg.value)>= minUSD);
        address2amount[msg.sender] += msg.value;
    }

    AggregatorV3Interface internal priceFeed;
    constructor() {
        priceFeed = AggregatorV3Interface(0x9326BFA02ADD2366b30bacB125260Af641031331);
    }
    function getLatestPrice() public view returns (int) {
        (,int price,,,) = priceFeed.latestRoundData();
        return price;
    }
    function getVersion() public view returns (uint256) {
        return priceFeed.version();
    }
    function getUSDRate(uint _ethAmount) public view returns (uint) {
        return uint((uint(getLatestPrice())*_ethAmount)/(10**8)); 
    }

}