
import { useEffect, useState } from 'react';
import Axios from 'axios'


function App() {

  const [data, setData] = useState([])

  useEffect(() => {
    Axios.get('http://localhost:5000/invernadero').then(
      (res) =>
        setData(res.data.controles))
  }, []);


  return (

    <div className="App">


      {data.map((data, index) => {
        return (
          <div key={index}>
            <div className="">
              <div className="">
                <h3 className="card-title">Id: <strong>{data.id}</strong></h3>
                <p className="card-text">Fecha: <strong>{data.fecha}</strong></p>
                <p className="card-text">humedad: <strong>{data.humedad}</strong></p>
                <p className="card-text">Medicion_agua: <strong>{data.medicion_agua}</strong></p>
                <p className="card-text">radiacion_solar: <strong>{data.radiacion_solar}</strong></p>
                <p className="card-text">radiacion_uv: <strong>{data.radiacion_uv}</strong></p>
                <p className="card-text">temperatura: <strong>{data.temperatura}</strong></p>
                <br/>
              </div>
            </div>
          </div>
        );
      })}

    </div>
  );
}

export default App;
