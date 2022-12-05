# create_advancements
進捗jsonをそれっぽく作る

## create_biome
冒険の時間用

csvをもとにそれっぽい進捗jsonを作る。
内容チェックはしていない。
itemaで、存在しないidを指定すると、それ以降は表示されないので注意。

|columns||
|-|-|
|name|名前
|parent|親にする進捗の名前
|item|アイコンに使うもののid
|nbt|アイコンのnbtタグ
|title|表示するタイトル
|frame|フレーム定義用だけどプログラムに反映していない
|description|表示する詳細情報
|criteria|訪れるバイオーム
|show_toast|トースト表示するか
|announce_to_chat|アナウンスするか

criteriaはbiomeのid
空指定すると、defaultは「slept_in_bed」をトリガーにしてある。（冒険の時間の初期に合わせる）
