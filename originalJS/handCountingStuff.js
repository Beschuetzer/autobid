   function getHighCardPoints(hand) {
    try {
      let pointCountsToUse = highCardPointValues.hcp;
      if (
        clientPreferences.pointCountingConvention.toLowerCase() === "alternative"
      ) {
        pointCountsToUse = highCardPointValues.alternative;
      }

      if (hand === undefined || hand === null) return -1;
      let points = 0;
      for (let i = 0; i < hand.length; i++) {
        const suit = hand[i];
        for (let j = 0; j < suit.length; j++) {
          const cardValue = suit[j];
          if (
            cardValue % 13 === 8 &&
            clientPreferences.pointCountingConvention.toLowerCase() ===
              "alternative" && suit.length >= suitLengthRequiredToCount.ten
          ) {
            points += pointCountsToUse.ten;
          } else if (cardValue % 13 === 9 && suit.length >= suitLengthRequiredToCount.jack) {
            points += pointCountsToUse.jack;
          } else if (cardValue % 13 === 10 && suit.length >= suitLengthRequiredToCount.queen) {
            points += pointCountsToUse.queen;
          } else if (cardValue % 13 === 11 && suit.length >= suitLengthRequiredToCount.king) {
            points += pointCountsToUse.king;
          } else if (cardValue % 13 === 12) {
            points += pointCountsToUse.ace;
          }
        }
        highCardPoints = points;
        highCardPointsLabel.innerHTML = points;
      }
    } catch (error) {
      console.error('error =', error);
    }
  }
  function getDistributionPoints(hand) {
    try {
      if (hand === undefined || hand === null) return -1;
      (clubsCount = 0), (diamondsCount = 0), (heartsCount = 0), (spadesCount = 0);
      (clubsHasNonHighCard = false),
        (diamondsHasNonHighCard = false),
        (heartsHasNonHighCard = false),
        (spadesHasNonHighCard = false);
      for (let i = 0; i < hand.length; i++) {
        getSuitCounts(hand[i]);
      }
      getDistributionPointsHelper();
    } catch (error) {
      console.error('error =', error);
    }
  }
  function getSuitCounts(suit) {
    try {
      if (suit === undefined || suit === null) return -1;
      for (let i = 0; i < suit.length; i++) {
        const card = suit[i];
        isNotHighCard =
          !card % 12 === 0 &&
          !card % 11 === 0 &&
          !card % 10 === 0 &&
          !card % 9 === 0;
        if (card >= 0 && card <= 12) {
          clubsCount++;
          if (isNotHighCard) {
            clubsHasNonHighCard = true;
          }
        } else if (card >= 13 && card <= 25) {
          diamondsCount++;
          if (isNotHighCard) {
            diamondsHasNonHighCard = true;
          }
        } else if (card >= 26 && card <= 38) {
          heartsCount++;
          if (isNotHighCard) {
            heartsHasNonHighCard = true;
          }
        } else if (card >= 39 && card <= 51) {
          spadesCount++;
          if (isNotHighCard) {
            spadesHasNonHighCard = true;
          }
        }
      }
    } catch (error) {
      console.error('error =', error);
    }
  }
  function getDistributionPointsHelper() {
    try {
      let points = 0;
      //===============================================================================
      //clubs
      if (clubsCount === 0) {
        points += distributionPointValues.shortness.void;
      } else if (clubsCount === 1) {
        points += distributionPointValues.shortness.singleton;
        // if (!clubsHasNonHighCard) points -= 1;
      } else if (clubsCount === 2) {
        points += distributionPointValues.shortness.doubleton;
      } else if (clubsCount > 4) {
        points += clubsCount - 4;
      }
      //===============================================================================
      //diamonds
      if (diamondsCount === 0) {
        points += distributionPointValues.shortness.void;
      } else if (diamondsCount === 1) {
        points += distributionPointValues.shortness.singleton;
        // if (!diamondsHasNonHighCard) points -= 1;
      } else if (diamondsCount === 2) {
        points += distributionPointValues.shortness.doubleton;
      } else if (diamondsCount > 4) {
        points += diamondsCount - 4;
      }
      //===============================================================================
      //hearts
      if (heartsCount === 0) {
        points += distributionPointValues.shortness.void;
      } else if (heartsCount === 1) {
        points += distributionPointValues.shortness.singleton;
        // if (!heartsHasNonHighCard) points -= 1;
      } else if (heartsCount === 2) {
        points += distributionPointValues.shortness.doubleton;
      } else if (heartsCount > 4) {
        points += heartsCount - 4;
      }
      //===============================================================================
      //spades
      if (spadesCount === 0) {
        points += distributionPointValues.shortness.void;
      } else if (spadesCount === 1) {
        points += distributionPointValues.shortness.singleton;
        // if (!spadesHasNonHighCard) points -= 1;
      } else if (spadesCount === 2) {
        points += distributionPointValues.shortness.doubleton;
      } else if (spadesCount > 4) {
        points += spadesCount - 4;
      }
      distributionPoints = points;
      distributionPointsLabel.innerHTML = points;
    } catch (error) {
      console.error('error =', error);
    }
  }
  //#endregion