import QtQuick
import QtQuick.Window
import QtQuick.Controls
import Qt5Compat.GraphicalEffects
import "components"

Window {
    id: root
    width: 640
    height: 480
    visible: true
    title: qsTr("waffwhale")
    color: Style.darkGray

    visibility: "Maximized"

    Row {
        Item {
            property int radius: Style.radius * 2
            id: menu
            width: 100 + radius
            height: parent.height

            Rectangle {
                color: Style.accent
                anchors.fill: parent

                Rectangle {
                    color: Style.darkGray
                    height: parent.height
                    width: radius * 2
                    radius: menu.radius
                    x: parent.width - radius
                }
            }

            Column {
                spacing: 16
                width: parent.width - parent.radius
                anchors.verticalCenter: parent.verticalCenter

                ImageButton {
                    file: '../../assets/icons/grid.svg'
                    imageSize: 32
                    padding: 16
                    color: '#22000000'
                    radius: 8

                    inactiveColor: Style.text
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: 'Browse'
                    textSize: 14
                    textPadding: 8
                }

                ImageButton {
                    file: '../../assets/icons/disc.svg'
                    imageSize: 32
                    padding: 16
                    color: '#00000000'
                    radius: 8

                    inactiveColor: Style.text
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: 'Albums'
                    textSize: 14
                    textPadding: 8
                }

                ImageButton {
                    file: '../../assets/icons/user.svg'
                    imageSize: 32
                    padding: 16
                    color: '#00000000'
                    radius: 8

                    inactiveColor: Style.text
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: 'Artists'
                    textSize: 14
                    textPadding: 8
                }

                ImageButton {
                    file: '../../assets/icons/list.svg'
                    imageSize: 32
                    padding: 16
                    color: '#00000000'
                    radius: 8

                    inactiveColor: Style.text
                    anchors.horizontalCenter: parent.horizontalCenter

                    text: 'Playlists'
                    textSize: 14
                    textPadding: 8
                }

                ImageButton {
                    file: '../../assets/icons/rss.svg'
                    imageSize: 32
                    padding: 16
                    color: '#00000000'
                    radius: 8

                    inactiveColor: Style.text
                    anchors.horizontalCenter: parent.horizontalCenter

                    text: 'Radios'
                    textSize: 14
                    textPadding: 8
                }

                ImageButton {
                    file: '../../assets/icons/heart.svg'
                    imageSize: 32
                    padding: 16
                    color: '#00000000'
                    radius: 8

                    inactiveColor: Style.text
                    anchors.horizontalCenter: parent.horizontalCenter

                    text: 'Favourites'
                    textSize: 14
                    textPadding: 8
                }
            }
        }

        Column {
            property int margins: 77
            width: root.width - menu.width - panel.width
            height: root.height

            ScrollView {
                height: parent.height - controls.height
                width: controls.width
                x: parent.margins
                contentWidth: width
                clip : true
//                __wheelAreaScrollSpeed: 50

                Column {
                    id: main
                    anchors.fill: parent
                    leftPadding: 0
                    rightPadding: 0
                    padding: 32

                    Row {
                        width: parent.width
                        spacing: 32
                        bottomPadding: 32

                        Column {
                            width: parent.width / 3
                            spacing: 8

                            Text {
                                color: Style.text
                                text: qsTr("Recently listened")
                                font.pixelSize: 32
                                font.bold: true
                            }

                            Repeater {
                                model: 5
                                HistoryEntry {
                                    width: parent.width
                                }
                            }
                        }

                        Column {
                            width: parent.width / 3
                            spacing: 8

                            Text {
                                color: Style.text
                                text: qsTr("Recently favorited")
                                font.pixelSize: 32
                                font.bold: true
                            }

                            Repeater {
                                model: 5
                                HistoryEntry {
                                    width: parent.width
                                }
                            }
                        }
                    }

                    Text {
                        color: Style.text
                        text: qsTr("Recently added")
                        font.pixelSize: 32
                        font.bold: true
                    }

                    Grid {
                        id: recentlyAdded
                        width: parent.width
                        leftPadding: 0
                        rightPadding: 0
                        padding: 16
                        spacing: 16
                        columns: 5

                        Repeater {
                            model: 10

                            AlbumCard {
                                // TODO: Fix width to be contained in recentlyAdded
                                width: (recentlyAdded.width - recentlyAdded.spacing * (recentlyAdded.columns - 1)) / recentlyAdded.columns
                            }
                        }
                    }
                }
            }

            Controls {
                id: controls
                width: parent.width - 2 * parent.margins
                x: parent.margins
            }
        }

        Rectangle {
            id: panel
            width: 400
            height: parent.height
            color: Style.gray

            Rectangle {
                color: Style.darkGray
                radius: menu.radius
                width: radius * 2
                height: parent.height
                x: -radius
            }

            Column {
                anchors.fill: parent
                anchors.margins: 47
                spacing: 7

                RoundImage {
                    source: '../../assets/cover.jpg'
                    width: parent.width
                    height: width
                    radius: 17
                }

                Text {
                    text: qsTr('Saturday Night')
                    font.pixelSize: 24
                    color: Style.accent
                }

                Text {
                    text: qsTr('DeA.D. Alive! (Live) ')
                    font.pixelSize: 16
                    color: Style.text
                }

                Text {
                    text: qsTr('Misfits')
                    font.pixelSize: 12
                    color: Style.text
                }

                Text {
                    topPadding: 32
                    bottomPadding: 16
                    text: qsTr('Listening Queue')
                    font.pixelSize: 24
                    font.weight: Font.Black
                    color: Style.text
                }

                Column {
                    width: parent.width
                    spacing: 10

                    Rectangle {
                        width: parent.width
                        height: 48
                        color: '#00000000'
                        radius: 8

                        Row {
                            anchors.fill: parent
                            spacing: 4

                            RoundImage {
                                source: '../../assets/cover.jpg'
                                width: 48
                                height: width
                                radius: 8
                            }

                            Column {
                                anchors.verticalCenter: parent.verticalCenter
                                spacing: 4

                                Text {
                                    text: qsTr('Dig Up Her Bones')
                                    font.pixelSize: 15
                                    color: Style.text
                                }

                                Text {
                                    text: qsTr('Misfits')
                                    font.pixelSize: 13
                                    color: Style.textLight
                                }
                            }
                        }
                    }

                    Rectangle {
                        width: parent.width
                        height: 48
                        color: '#00000000'
                        radius: 8

                        Row {
                            anchors.fill: parent
                            spacing: 4

                            RoundImage {
                                source: '../../assets/cover.jpg'
                                width: 48
                                height: width
                                radius: 8
                            }

                            Column {
                                anchors.verticalCenter: parent.verticalCenter
                                spacing: 4

                                Text {
                                    text: qsTr('Helena')
                                    font.pixelSize: 15
                                    color: Style.text
                                }

                                Text {
                                    text: qsTr('Misfits')
                                    font.pixelSize: 13
                                    color: Style.textLight
                                }
                            }
                        }
                    }

                    Rectangle {
                        width: parent.width
                        height: 48
                        color: Style.lightGray
                        radius: 8

                        Row {
                            anchors.fill: parent
                            spacing: 4

                            RoundImage {
                                source: '../../assets/cover.jpg'
                                width: 48
                                height: width
                                radius: 8
                            }

                            Column {
                                anchors.verticalCenter: parent.verticalCenter
                                spacing: 4

                                Text {
                                    text: qsTr('Saturday Night')
                                    font.pixelSize: 15
                                    color: Style.accent
                                }

                                Text {
                                    text: qsTr('Misfits')
                                    font.pixelSize: 13
                                    color: Style.text
                                }
                            }
                        }
                    }
                }
            }

        }
    }

}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.66;height:1080;width:1920}
}
##^##*/
