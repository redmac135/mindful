import React, { Component } from 'react';
import ReactDOM from 'react-dom/client';
import { Animated } from 'react-native';

const c = new Animated.Value(0);

class App extends Component {
    render() {
        React.useEffect(() => {
            Animated.loop(
                Animated.timing(c, {
                    toValue: 300,
                    duration: 3000,
                }),
                { iterations: 5 }
            ).start();
        }, []);

        const animatedColor = c.interpolate({
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

reportWebVitals();