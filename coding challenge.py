{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOAdy6BQVSmngv3cQbPl7IW",
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
        "<a href=\"https://colab.research.google.com/github/kartikhatwaliya/Davistraining-/blob/main/coding%20challenge.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "dVFKolRCHz8T"
      },
      "outputs": [],
      "source": [
        "#question-1\n",
        "price = float(input(\"Enter price: \"))\n",
        "discount = float(input(\"Enter discount percentage: \"))\n",
        "\n",
        "final_price = price - (price * discount / 100)\n",
        "\n",
        "print(\"Final price after discount:\", final_price)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Question-2\n",
        "age = int(input(\"Enter age: \"))\n",
        "\n",
        "if age >= 18:\n",
        "    print(\"Eligible\")\n",
        "else:\n",
        "    print(\"Not Eligible\")"
      ],
      "metadata": {
        "id": "bmLMZXCvMH0M"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Question-3\n",
        "units = int(input(\"Enter units: \"))\n",
        "\n",
        "if units <= 100:\n",
        "    bill = units * 1.5\n",
        "elif units <= 200:\n",
        "    bill = units * 2.5\n",
        "else:\n",
        "    bill = units * 4\n",
        "\n",
        "print(\"Total bill amount:\", bill)"
      ],
      "metadata": {
        "id": "S-1juTIrNIDJ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Question-4\n",
        "n = int(input(\"Enter N: \"))\n",
        "\n",
        "print(\"Even numbers:\")\n",
        "for i in range(1, n + 1):\n",
        "    if i % 2 == 0:\n",
        "        print(i, end=\" \")"
      ],
      "metadata": {
        "id": "ISfCislVNqzk"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Question-5\n",
        "def simple_interest(p, r, t):\n",
        "    si = (p * r * t) / 100\n",
        "    return si\n",
        "\n",
        "p = float(input(\"Enter Principal: \"))\n",
        "r = float(input(\"Enter Rate: \"))\n",
        "t = float(input(\"Enter Time: \"))\n",
        "\n",
        "print(\"Simple Interest:\", simple_interest(p, r, t))"
      ],
      "metadata": {
        "id": "l5GeuVPxOAaC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ePQwP5dAOzn8"
      },
      "outputs": [],
      "source": [
        "#question-6\n",
        "price = float(input(\"Enter price: \"))\n",
        "discount = float(input(\"Enter discount percentage: \"))\n",
        "\n",
        "final_price = price - (price * discount / 100)\n",
        "\n",
        "print(\"Final price after discount:\", final_price)"
      ]
    }
  ]
}