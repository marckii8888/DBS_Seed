import React, { useState } from 'react';
import { useEffect } from 'react';
import productlist from '../datajson/products.json';

const Product = (props) => {

    const {id} = props.match.params;
    const [product, setProduct] = useState({});

    useEffect(() => {
        const findProduct = productlist.filter(product => product.id == id);
        setProduct(findProduct[0]);
        console.log(product);
    });

    if (!product.title) { return <div>Loading...</div>}

    return (
        
        <div className="item">
            <h3>{product.title}</h3>
            <img className="ui image" src={product.image} alt={product.title}/>
            <h4>{product.price}</h4>
            <h4>{product.description}</h4>
        </div>
    )
}

export default Product;