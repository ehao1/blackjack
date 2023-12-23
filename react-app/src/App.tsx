import ListGroup from './components/ListGroup';
import { useState } from 'react';

function App() {
  const [card, setcardText] = useState('no card yet');

  return (
    <>
      <ListGroup onClickFunc={setcardText} />
      <h1>{card}</h1>
    </>
  );
}

export default App;
