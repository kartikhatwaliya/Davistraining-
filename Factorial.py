{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP5FG91EFYHEROpOK22T0Nu",
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
        "<a href=\"https://colab.research.google.com/github/kartikhatwaliya/Davistraining-/blob/main/Factorial.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
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
        "# find kro greatest number\n",
        "a = int(input(\"Enter a nummber \"))\n",
        "fact = 1\n",
        "if(a<0):\n",
        "    print(\"factorial is not possible \")\n",
        "elif(a==0 or a==1):\n",
        "    print(\"factorial is \"+1)\n",
        "else:\n",
        "    for x in range(2,a+1):\n",
        "        fact = fact * x ;\n",
        "    print(\"factorial of \",a, \"is\", fact)\n",
        "\n",
        ""
      ]
    }
  ]
}