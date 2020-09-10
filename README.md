[![CircleCI](https://circleci.com/gh/syou6162/tmu_cs2_2020.svg?style=shield)](https://circleci.com/gh/syou6162/tmu_cs2_2020)

# 東京都立大学 情報科学特論2
吉田が担当した分の講義資料です。

- [講義資料](https://docs.google.com/presentation/d/1LWSENPWdwkG3LnxnRWEmL9xldHwdhg-52EDWv4m9MDU)
- [提出課題用資料](https://colab.research.google.com/drive/1XiSMhsHM0w5SUY45AR4xtinFDujBEtO6)


## 課題データのダウンロード

```
make download-kdd-data
```

実行後、`data`ディレクトリ以下に`train.pickle`と`test.pickle`ができていることを確認しましょう。

## テストの実行

```
make test
```

## 課題提出の前には
以下を実行して正常に動くことを確認しましょう。

```
make format lint test
```

## 参考: Docker上での実行
2020年の講義ではDocker上での実行ではなく、Google Colab上での実行をします。もし、Dockerを使った開発を手元で体験したい人がいたら、以下を手元で実行してみましょう。

- [Install Docker Desktop on Windows | Docker Documentation](https://docs.docker.com/docker-for-windows/install/)

### Dockerイメージのビルド

```sh
docker build -f Dockerfile -t tmu_cs2 .
```

### Dockerコンテナの実行

```
docker run --rm -ti -v $PWD/anomaly_detection:/app/anomaly_detection -v $PWD/tests:/app/tests -v $PWD/data:/app/data -p 5000:5000 tmu_cs2
```

これ以降のコマンドはDockerコンテナ上で実行してください。
