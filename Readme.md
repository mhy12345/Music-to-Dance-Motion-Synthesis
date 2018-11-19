# Dataset

## Introduction

This dataset is build to create relationship between dance motion and the music, which contains four types of dance, Cha-cha, Tango, Rumba and Waltz. 

In each directory, `audio.mp3` gives the audio files of the dance. `skeletons.json` describes the skeleton points of the dance, the `config.json` gives the start frames and the end frames (The dance sequence match part of the songs). The FPS of the dataset is 25 frames per second.


## Paper

This dataset is build along with the ACM-Multimedia regular paper & demo paper:

```
@inproceedings{tang2018dance,
	title={Dance with Melody: An LSTM-autoencoder Approach to Music-oriented Dance Synthesis},
	author={Tang, Taoran and Jia, Jia and Mao, Hanyang},
	booktitle={2018 ACM Multimedia Conference on Multimedia Conference},
	pages={1598--1606},
	year={2018},
	organization={ACM}
}
```

```
@inproceedings{tang2018anidance,
	title={AniDance: Real-Time Dance Motion Synthesize to the Song},
	author={Tang, Taoran and Mao, Hanyang and Jia, Jia},
	booktitle={2018 ACM Multimedia Conference on Multimedia Conference},
	pages={1237--1239},
	year={2018},
	organization={ACM}
}
```

## FAQs

### Why there are 23 points in the dataset, but only 21 was mentioned in the paper.

Our model in the regular paper was built with the dataset containing 21 skeleton points. However, in the demo paper, when we try to use Unity to build a 3D model. We realized that the direction of the hands can not be well described. The extra points (#22 & #23) are used to describe the position of the hands.


## Notes

Let me know if something is wrong with the dataset.

Issues posted in [public repository](https://github.com/Music-to-dance-motion-synthesis/dataset) will not be noticed. If you have any question, please email [me](maohanyang789@163.com), or create an issue in [https://github.com/mhy12345/Music-to-Dance-Motion-Synthesis](https://github.com/mhy12345/Music-to-Dance-Motion-Synthesis).
