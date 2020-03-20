import React from "react";
import '../view/Home.css'

const showScore = (arrScore) => {

    return arrScore.map( (score, index) => {

        return (
            <li className={'container__score__element'}
                key={index} >
                <p className={'container__score__data'}>
                    HOME:  {score.HOME}
                </p>
                <p className={'container__score__data'}>
                    AWAY:  {score.AWAY}
                </p>
                <p className={'container__score__data'}>
                    WIN:  {score.WIN}
                </p>
            </li>)

    })
};



const Score = props => {
  return (
      <div >
          {showScore(props.score)}
      </div>
  )
};

export default Score;