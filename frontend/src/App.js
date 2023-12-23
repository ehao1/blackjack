import './App.css';
import axios from 'axios';
import {useState, useEffect} from 'react';

function App() {
  const [cards, setCards] = useState([]);

  useEffect(()=> {
    axios.get('http://localhost:8000/api').then(res => setCards(res.data))
  }, []);

  console.log(cards);
  return(cards.map((card, index) => {
    return <DisplayCard key={index} card={card}/>
  }));
}

// "TODO: Figure out style guidelines for react comments"
// "This function takes in a card and displays it properly"
function DisplayCard(props){
  const card = props.card;
  const index = props.index;
  var value = card[0];
  var suit = card[1];
  if (suit == 4) {
    suit = "of Diamonds";
  } else if (suit == 3){
    suit = "of Clubs";
  } else if (suit == 2){
    suit = "of Hearts";
  } else {
    suit = "of Spades";
  }

  


  return (<p key={index}> {value} {suit} </p>);
}


export default App;
