import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';
import { TouchableOpacity, Animated } from 'react-native';

const ButtonWithSpin = () => {
  const [rotateAnimation, setRotateAnimation] = useState(new Animated.Value(0));

  const handleAnimation = () => {
    Animated.timing(rotateAnimation, {
      toValue: 1,
      duration: 800,
    }).start(() => {
      rotateAnimation.setValue(0);
    });
  };

  const interpolateRotating = rotateAnimation.interpolate({
    inputRange: [0, 1],
    outputRange: ['0deg', '720deg'],
  });

  const animatedStyle = {
    transform: [
      {
        rotate: interpolateRotating,
      },
    ],
  };

  return (
    <TouchableOpacity
      onPress={async () => handleAnimation()}
      style={{ width: 60 }}
    >
      <Animated.Text style={animatedStyle}>Click me</Animated.Text>
    </TouchableOpacity>
  );
};

export default ButtonWithSpin;

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        <ButtonWithSpin />
    </React.StrictMode>
);