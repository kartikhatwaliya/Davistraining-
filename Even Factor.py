{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM5t8hRteJM2Dk1jb0UN5b0",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/kartikhatwaliya/Davistraining-/blob/main/Even%20Factor.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "aKk4OFqp6Lgx"
      },
      "outputs": [],
      "source": [
        "# Display even factor of a number\n",
        "a = int(input(\"Enter a nummber \"))\n",
        "a = abs(a)\n",
        "if(a==0):\n",
        "    print(0)\n",
        "else:\n",
        "    for x in range( 2,(a//2)+1):\n",
        "        if(a%x == 0 and x%2==0):\n",
        "            print(x)\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        ""
      ]
    }
  ]
}