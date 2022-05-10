import React, { Component, useState } from 'react';
import ReactDOM from 'react-dom/client';
import { Animated } from 'react-native';
class App extends Component {
    render() {

        const [color, setColor ] = useState(Animated.Value(0));
        
        setColor(() => {
            Animated.loop(
                Animated.timing(color, {
                    toValue: 300,
                    duration: 3000,
                }),
                { iterations: 5 }
            ).start();
        }, []);

        const animatedColor = color.interpolate({
            inputRange: [0, 200, 300],
            outputRange: ['orange', 'lightgreen', 'yellow'],
        });

        return (
            <Animated.View style={{ backgroundColor: animatedColor }}>
                <h1>Hi There!</h1>
            </Animated.View>
        );
    }
};

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
);