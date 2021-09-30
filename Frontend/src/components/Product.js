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
            <h2 className="ui center aligned container">{product.title}</h2>
            <img className="ui medium rounded centered image" src={product.image} alt={product.title}/>
            <h2 className="ui center aligned container">Price: ${product.price}</h2>
            <h4>{product.description}</h4>
        </div>
    )
}

export default Product;