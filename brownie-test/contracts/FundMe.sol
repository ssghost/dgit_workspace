// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract FundMe {
    mapping (address => uint) public address2amount;
    address[] public funders;
    function recvFund() public payable {
        uint minUSD = 5*10**8;
        require(getUSDRate(msg.value)>= minUSD);
        address2amount[msg.sender] += msg.value;
        funders.push(msg.sender);
    }

    address public owner = msg.sender;
    modifier ownerChecker {require(owner == msg.sender); _;}
    function witdFund() public payable ownerChecker {
        payable(msg.sender).transfer(address(this).balance);
        for (uint i=0; i<funders.length; i++) {
            address2amount[funders[i]] = 0;
        }
        funders = new address[](0);
    }

    AggregatorV3Interface internal priceFeed;
    constructor(address _priceFeed) {
        priceFeed = AggregatorV3Interface(_priceFeed);
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
    function getEntranceFee() public view returns (uint256) {
        uint256 minimumUSD = 50 * 10**18;
        uint256 price = uint(getLatestPrice());
        uint256 precision = 1 * 10**18;
        return ((minimumUSD * precision) / price) + 1;
    }
}