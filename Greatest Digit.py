{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNrbRm8+DwcQ8r4ULbkBAha",
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
        "<a href=\"https://colab.research.google.com/github/kartikhatwaliya/Davistraining-/blob/main/Greatest%20Digit.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
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
        "# find greatest digit\n",
        "a = int(input(\"Enter a nummber \"))\n",
        "a = abs(a)\n",
        "gd = 0\n",
        "if(a==0):\n",
        " print(\"Greatest digit is \",a)\n",
        "\n",
        "\n",
        "else:\n",
        "  while(a!=0):\n",
        "      ld = a%10\n",
        "      if(ld>gd):\n",
        "          gd = ld\n",
        "      a = a//10\n",
        "\n",
        "\n",
        "  print(\"Greatest digit is\",gd)"
      ]
    }
  ]
}