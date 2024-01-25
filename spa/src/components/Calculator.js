import React, { useState } from 'react';
import axios from 'axios';

const CalculatorApp = () => {
    const [numbersInput, setNumbersInput] = useState([]);
    const [operator, setOperator] = useState('add');
    const [result, setResult] = useState(null);

    const handleNumbersInputChange = (e) => {
        setNumbersInput(e.target.value);
        console.log(numbersInput)
    };

    const handleOperatorChange = (e) => {
        setOperator(e.target.value);
    };

    const calculateResult = async () => {
        const numbersArray = numbersInput.split(',').map((num) => parseFloat(num.trim().replace(',', '.')));
        console.log(numbersArray)
        console.log(operator)

        try {
            const response = await axios.post('http://localhost:8000/calculate', {
                numbers: numbersArray,
                operator: operator,
            });

            setResult(response.data.result);
        } catch (error) {
            console.error('Error calculating result:', error);
        }
    };

    return (
        <div>
            <h1>Rechner</h1>
            <div>
                <label>
                    Zahlen:
                    <input type="text" value={numbersInput} onChange={handleNumbersInputChange} />
                </label>
            </div>
            <div>
                <label>
                    Operator:
                    <select onChange={handleOperatorChange}>
                        <option value="add">+</option>
                        <option value="subtract">-</option>
                        <option value="multiply">*</option>
                        <option value="divide">/</option>
                    </select>
                </label>
            </div>
            <div>
                <button onClick={calculateResult}>Berechnen</button>
            </div>
            {result !== null && (
                <div>
                    <h2>Ergebnis: {result}</h2>
                </div>
            )}
        </div>
    );
};

export default CalculatorApp;
