import React from 'react';
import './Table.css';

function Table({tableData}){
    const translate = {
		"pt": {
			"data": "Data",
			"op" : "Operação",
            "saldo" : "Saldo",
            "desc" : "Descrição",
		},
		"en": {
			"data" : "Date",
			"op": "Operation",
            "saldo" : "Balance",
            "desc" : "Description",
		},
		"es": {
			"data" : "Fecha",
			"op": "Operación",
            "saldo" : "Saldo",
            "desc" : "Descripción",
		}
	}

    var lang = localStorage.getItem('lang');

    return(
        <table className='table'>
            <thead className='thead'>
                <tr className='tr-head'>
                    <th className='th'>{translate[lang]['data']}</th>
                    <th className='th'>{translate[lang]['op']}</th>
                    <th className='th'>{translate[lang]['saldo']}</th>
                    <th className='th'>{translate[lang]['desc']}</th>
                </tr>
            </thead>
            <tbody className='tbody'>
                {tableData.map((value, index)=>{
                    return(
                        <tr className='tr-body' key={index}>
                            <td className='td'>{value.date}</td>
                            <td className='td'>{value.value}</td>
                            <td className='td'>{value.saldoapos}</td> {/* TODO mudar para saldo */}
                            <td className='td'>{value.description}</td>
                        </tr>
                    )
                })}
            </tbody>
        </table>
    )
}
export default Table;