#!/usr/bin/env python3
# coding: utf-8

from tkinter import *
import pprint

# CONSTANTES

# Dimensions du plateau de jeu
NB_LIGNES = 9
NB_COLONNES = 7

# Largeur/Hauteur d'une case du plateau
D = 51

# Types de case
TERRE = 0
EAU = 1
PIEGE_BLANC = 2
PIEGE_NOIR = 3
TANIERE_BLANC = 4
TANIERE_NOIR = 5


# VARIABLES GLOBALES du Jeu

# Représentation mémoire du plateau de jeu (9 x 7 cases : Tuple de tuples qui peut-être vu comme un tableau 2 dimensions)
plateau = (
		( TERRE , TERRE , PIEGE_NOIR , TANIERE_NOIR , PIEGE_NOIR , TERRE , TERRE ) ,
		( TERRE , TERRE , TERRE , PIEGE_NOIR , TERRE , TERRE , TERRE ) ,
		( TERRE , TERRE , TERRE , TERRE , TERRE , TERRE , TERRE ) ,
		( TERRE , EAU , EAU , TERRE , EAU , EAU , TERRE ) ,
		( TERRE , EAU , EAU , TERRE , EAU , EAU , TERRE ) ,
		( TERRE , EAU , EAU , TERRE , EAU , EAU , TERRE ) ,
		( TERRE , TERRE , TERRE , TERRE , TERRE , TERRE , TERRE ) ,
		( TERRE , TERRE , TERRE , PIEGE_BLANC , TERRE , TERRE , TERRE ) ,
		( TERRE , TERRE , PIEGE_BLANC , TANIERE_BLANC , PIEGE_BLANC , TERRE , TERRE )
	)
	
	
# Pions : Force et position initiale
pionsDuJeu = {
	'rat' : {
				'force' : 1 ,
				'position' : {
						'noir' : ( 3 , 1 ) ,
						'blanc' : ( 7 , 7 )
					}
		} ,
	'chat' : {
				'force' : 2 ,
				'position' : {
						'noir' : ( 2 , 6 ) ,
						'blanc' : ( 8 , 2 )
					}
		} ,
	'loup' : {
				'force' : 3 ,
				'position' : {
						'noir' : ( 3 , 5 ) ,
						'blanc' : ( 7 , 3 )
					}
		} ,
	'chien' : {
				'force' : 4 ,
				'position' : {
						'noir' : ( 2 , 2 ) ,
						'blanc' : ( 8 , 6 )
					}
		} ,
	'panthère' : {
				'force' : 5 ,
				'position' : {
						'noir' : ( 3 , 3 ) ,
						'blanc' : ( 7 , 5 )
					}
		} ,
	'tigre' : {
				'force' : 6 ,
				'position' : {
						'noir' : ( 1 , 7 ) ,
						'blanc' : ( 9 , 1 )
					}
		} ,
	'lion' : {
				'force' : 7 ,
				'position' : {
						'noir' : ( 1 , 1 ) ,
						'blanc' : ( 9 , 7 )
					}
		} ,
	'éléphant' : {
				'force' : 8 ,
				'position' : {
						'noir' : ( 3 , 7 ) ,
						'blanc' : ( 7 , 1 )
					}
		}
	}

	
# Identifiants des cases et occupants
cases = []

	
# Pions dans la partie
pions = {
		'noir' : {} ,
		'blanc' : {}
	}


# FONCTIONS

def creerGUI() :
	
	global fenetre , plateauGUI
	
	fenetre = Tk()
	fenetre.title( 'pyXouDouQi' )
	
	plateauGUI = Canvas( fenetre )
	plateauGUI[ 'width'] = 365
	plateauGUI[ 'height'] = 469
	plateauGUI[ 'background' ] = 'black'
	
	plateauGUI.pack( side = LEFT , fill = BOTH , pady = 2 , padx = 2 )
	
	

def initialiserPions() :
	for nom in pionsDuJeu.keys() :
		pions[ 'noir' ][ nom ] = {}
		pions[ 'noir' ][ nom ][ 'position' ] = pionsDuJeu[ nom ][ 'position' ][ 'noir' ]
		pions[ 'blanc' ][ nom ] = {}
		pions[ 'blanc' ][ nom ][ 'position' ] = pionsDuJeu[ nom ][ 'position' ][ 'blanc' ]



def selectionnerPion( event ) :
	idPion = event.widget.find_closest( event.x , event.y )[0]
	print( idPion )
	print( plateauGUI.gettags( idPion )[0] )
	
	
def selectionnerCase( event ) :
	idCase = event.widget.find_closest( event.x , event.y )[0]
	print( idCase )
	print( plateauGUI.gettags( idCase )[0] )
	
	
	
def dessinerPion( couleur , nom ) :
	ligne = pionsDuJeu[ nom ][ 'position' ][ couleur ][ 0 ]
	colonne = pionsDuJeu[ nom ][ 'position' ][ couleur ][ 1 ]
	
	x = D * colonne - D + colonne + D // 2 + 1
	y = D * ligne - D + ligne + D // 2 + 1
	
	if couleur == 'noir' :
		pions[ couleur ][ nom ][ 'id' ] = plateauGUI.create_text( x , y , text = str( pionsDuJeu[ nom ][ 'force' ] ) , font = ( 'TkDefaultFont' , '30' , 'bold'  ) , fill = 'black' , tags = '{}-{}'.format( couleur , nom ) )
	else :
		pions[ couleur ][ nom ][ 'id' ] = plateauGUI.create_text( x , y , text = str( pionsDuJeu[ nom ][ 'force' ] ) , font = ( 'TkDefaultFont' , '30' , 'bold'  ) , fill = 'white' , tags = '{}-{}'.format( couleur , nom ) )
		
	plateauGUI.tag_bind( pions[ couleur ][ nom ][ 'id' ] , '<Button-1>' , selectionnerPion )
		
	cases[ ligne - 1 ][ colonne - 1 ][ 'occupant' ] = { 'couleur' : couleur , 'nom' : nom }

	
	
def positionnerPions() :
	# Question 4.7
	# Votre code ici
	pass
	
	
		
	
	
	
def dessinerCase( ligne , colonne , typeCase = TERRE ) :

	x1 = D * colonne - D + colonne + 1
	x2 = ( D + 1 ) * colonne
	
	y1 = D * ligne - D + ligne + 1
	y2 = ( D + 1 ) * ligne
	
	if typeCase == TERRE :
		idCase = plateauGUI.create_rectangle( x1 , y1 , x2 , y2 , outline = 'green' , fill = 'green' , tags = '{}-{}'.format( ligne , colonne ) )
		
	elif typeCase == EAU :
		idCase = plateauGUI.create_rectangle( x1 , y1 , x2 , y2 , outline = 'blue' , fill = 'blue' , tags = '{}-{}'.format( ligne , colonne ) )
		
	elif typeCase == PIEGE_BLANC or typeCase == PIEGE_NOIR :
		idCase = plateauGUI.create_rectangle( x1 , y1 , x2 , y2 , outline = 'green' , fill = 'green' , stipple = 'gray50' , tags = '{}-{}'.format( ligne , colonne ) )
		
	elif typeCase == TANIERE_BLANC or typeCase == TANIERE_NOIR :
		idCase = plateauGUI.create_rectangle( x1 , y1 , x2 , y2 , outline = 'green' , fill = 'green' , stipple = 'gray75' , tags = '{}-{}'.format( ligne , colonne ) )

	plateauGUI.tag_bind( idCase , '<Button-1>' , selectionnerCase )
	
	return idCase




def dessinerPlateau() :
	print( '\nQuestion 3.3' )
	for i in range( NB_LIGNES ) :
		cases.append( [] )
		for j in range( NB_COLONNES) :
			cases[ -1 ].append( { 'occupant' : None } )
			cases[ -1 ][ -1 ][ 'id' ] = dessinerCase( i + 1 , j + 1 , plateau[ i ][ j ] )
			
			# Question 3.3
			# Votre code ici
			
			
			
def debugPlateau() :
	print( '\nPlateau :\n' )
	for i in range( NB_LIGNES ) :
		for j in range( NB_COLONNES ) :
			if cases[ i ][ j ][ 'occupant' ] == None :
				print( '*'.center( 15 ) , end = '' )
			else :
				strPion = cases[ i ][ j ][ 'occupant' ][ 'couleur' ] + '-' + cases[ i ][ j ][ 'occupant' ][ 'nom' ]
				print( strPion.center( 15 ) , end = '' )
		print( '' )
	print( '' )
	


# ENTRÉE DU PROGRAMME

if __name__ == '__main__' :
	
	creerGUI()
	dessinerPlateau()
	
	# L'instruction qui suit permet d'afficher une représentation
	# tabulaire de la variable "cases". 
	print( '\nVariable "cases" :' )
	pprint.PrettyPrinter( indent = 4 ).pprint( cases )
	
	
	# Question 4.5
	print( '\nQuestion 4.5' )
	# Votre code ici
		
		
	
	# Question 4.6
	print( '\nQuestion 4.6' )
	# Votre code ici
	
	
	initialiserPions()
	positionnerPions()
	
	# Question 4.8
	print( '\nQuestion 4.8' )
	print( '\nVariable "cases" :' )
	# Votre instruction ici
	
	
	# Question 4.9
	print( '\nQuestion 4.9' )
	print( '\nVariable "pions" :' )
	# Votre instruction ici
	
	
	fenetre.mainloop()
	
