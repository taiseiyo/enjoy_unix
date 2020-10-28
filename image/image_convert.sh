#!/bin/bash # シェバン

for img in *.png; do # ワイルドカード
    name=${img/.png/""} # 変数展開(Variable expansion)
    convert "$name".png -resize 180x180! "$name"_new.png # イメージマジック
    echo $(file "$name"_new.png)
done
