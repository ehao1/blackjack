import axios from 'axios';

interface Props {
  onClickFunc: React.Dispatch<React.SetStateAction<string>>;
}

function ListGroup(props: Props) {
  function drawCard() {
    axios.get(`http://localhost:8000/drawCard`).then((res) => {
      props.onClickFunc(res.data);
    });
  }

  return (
    <>
      <button type='button' className='btn btn-primary' onClick={drawCard}>
        Draw a card
      </button>
    </>
  );
}

export default ListGroup;
